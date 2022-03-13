import pandas as pd
import json
import datetime


print(datetime.datetime.now())

    
with open("data/json/reformatted_nonli.json", "r") as f:
    data_reformatted_nonli = json.load(f)
    
    
def json_to_pandas(data_json, schema, column):

    df = pd.DataFrame(columns = schema)

    for i, item in enumerate(data_json):

        print('{} / {}'.format(i+1, len(data_json)), end="\r")

        df_batch = pd.DataFrame(columns = schema)

        for item_column in item[column]:
            row = [item['org_uuid'], *[item_column[title] for title in schema[1:]]]
            df_batch = pd.concat(
                [
                    df_batch, 
                    pd.DataFrame([row], columns=schema)
                ]
            )

        df = pd.concat([df, df_batch])
        
    print('DataFrame {0} size : {1}'.format(column, df.shape[0]))
    
    return df


education_schema = [
        'org_uuid', 
        'education_school_name', 
        'education_field_of_study',
        'education_description',
        'education_degree',
        'education_start_date_year',
        'education_end_date',
        'education_school_link'
    ]

experience_schema = [
        'org_uuid', 
        'experience_title', 
        'experience_start_date',
        'experience_end_date',
        'experience_headcount_range',
        'experience_company_name',
        'experience_company_link',
        'experience_company_id_link',
        'experience_industry',
        'experience_location',
        'experience_description'
    ]

skills_schema = [
        'org_uuid', 
        'skill',
    ]


json_to_pandas(
    data_json=data_reformatted_nonli,
    schema=education_schema, 
    column='educations'
).to_csv('data/uuid_x_education_fields.csv')


json_to_pandas(
    data_json=data_reformatted_nonli,
    schema=experience_schema, 
    column='experiences'
).to_csv('data/uuid_x_experience_fields.csv')


json_to_pandas(
    data_json=data_reformatted_nonli,
    schema=skills_schema, 
    column='skills'
).to_csv('data/uuid_x_skills_fields.csv')
