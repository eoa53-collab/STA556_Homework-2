def fill_missing_values(data):
    """
    Replaces missing categorical values with 'Unknown'.

    """

    clean_data = data.copy()

    missing_columns = [
        "Teacher_Quality",
        "Parental_Education_Level",
        "Distance_from_Home"
    ]

    for column in missing_columns:
        clean_data[column] = clean_data[
            column
        ].fillna("Unknown")

    return clean_data



def filter_records(data):
    """
    Keeps observations with exam scores between 0 and 100 by removing records with exam scores outside the expected 0 - 100 range
    """

    filtered_data = data.loc[
        (data["Exam_Score"] >= 0) &
        (data["Exam_Score"] <= 100)
    ].copy()

    return filtered_data


def summarize_group(data, group_col):
    """
    Return the number of students and mean exam score by group.
    """

    summary = (
        data.groupby(group_col)["Exam_Score"]
        .agg(["count", "mean"])
        .reset_index()
    )

    return summary

