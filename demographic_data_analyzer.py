import pandas as pd


def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv")
    race_count = df["race"].value_counts()
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)
    percentage_bachelors = round(
        df["education"].value_counts(normalize=True).get("Bachelors", 0) * 100, 1
    )
    advanced_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    high_earners = advanced_education[advanced_education["salary"] == ">50K"]
    percentage_advance_high_earners = round(
        high_earners.shape[0] / advanced_education.shape[0] * 100, 1
    )
    non_advanced_education = df[
        ~df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    ]
    non_advance_high_earners = non_advanced_education[
        non_advanced_education["salary"] == ">50K"
    ]
    percentage_non_advance_high_earners = round(
        non_advance_high_earners.shape[0] / non_advanced_education.shape[0] * 100, 1
    )
    higher_education_rich = percentage_advance_high_earners
    lower_education_rich = percentage_non_advance_high_earners
    min_work_hours = df["hours-per-week"].min()
    min_workers = df[df["hours-per-week"] == min_work_hours]
    total_min_workers = len(min_workers)
    min_workers_high_salary = len(min_workers[min_workers["salary"] == ">50K"])
    percentage_high_salary = (min_workers_high_salary / total_min_workers) * 100

    num_min_workers = total_min_workers

    rich_percentage = percentage_high_salary
    country_high_earners = (
        df[df["salary"] == ">50K"].groupby("native-country").size()
        / df.groupby("native-country").size()
        * 100
    )
    highest_percentage_country = country_high_earners.idxmax()

    highest_earning_country = highest_percentage_country
    highest_earning_country_percentage = round(country_high_earners.max(), 1)
    top_IN_occupation = (
        df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
        .groupby("occupation")
        .size()
        .idxmax()
    )

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
