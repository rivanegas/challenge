table_schemas = {
    'hired_employees': [
        'id INTEGER PRIMARY KEY',
        'name VARCHAR(100)',
        'datetime VARCHAR(100)',
        'department_id FLOAT',
        'job_id FLOAT'
    ],
    'departments': [
        'id INTEGER PRIMARY KEY',
        'department VARCHAR(100)'
    ],
    'jobs': [
        'id INTEGER PRIMARY KEY',
        'job VARCHAR(100)'
    ]
}