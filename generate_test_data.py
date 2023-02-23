from faker import Faker
import random
import pandas as pd
from sqlalchemy import create_engine


fake = Faker()

# Define variables


# Create data
def test_data(projects, pms=10, gen_start_date="-2y", gen_end_date="-1y"):
    project_manager_list = []
    project_manager = []
    project_id = []
    source_language = []
    target_language = []
    word_count = []
    segment_count = []
    completion_rate = []
    tm_leverage = []
    translation_quality = []
    project_cost = []
    project_revenue = []
    start_date = []
    end_date = []
    status = []

    # Generate PMs
    for _ in range(pms):
        project_manager_list.append(fake.name())

    for _ in range(projects):
        project_manager.append(random.choice(project_manager_list))
        project_id.append(fake.unique.bothify(text="######"))

        # Make sure source_language != target_language
        source_language.append(fake.locale())
        check_target_language = fake.locale()
        while check_target_language == source_language:
            check_target_language = fake.locale()

        target_language.append(check_target_language)

        segment_count.append(fake.random_int(100, 2500))
        word_count.append(segment_count[-1] * fake.random_int(5, 25))
        completion_rate.append(random.choice([100, fake.random_int(85, 100)]))
        tm_leverage.append(fake.random_int(0, 100))
        translation_quality.append(fake.random_int(89, 100))
        project_cost.append(word_count[-1] * fake.random_int(15, 55))

        start_date.append(fake.date_time_between_dates(gen_start_date, gen_end_date))

        end_date.append(fake.date_time_between_dates(start_date[-1], gen_end_date))
        status.append("Complete")

    all_data = pd.DataFrame(
        {
            "project_manager": project_manager,
            "project_id": project_id,
            "source_language": source_language,
            "target_language": target_language,
            "segment_count": segment_count,
            "word_count": word_count,
            "completion_rate": completion_rate,
            "tm_leverage": tm_leverage,
            "translation_quality": translation_quality,
            "project_cost": project_cost,
            "start_date": start_date,
            "end_date": end_date,
            "status": status,
        }
    )

    return all_data


if __name__ == "__main__":
    # Create Engine for creating file
    engine = create_engine("sqlite:///Dummy_data.db")

    # Get dummy data:
    data = test_data(50)

    # Add data to the database
    data.to_sql("localization_projects", con=engine, if_exists="replace", index=False)
