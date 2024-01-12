# Diz Package

This is the `diz` package. It contains the `Diz` class and the `LABVALUE` dataclass.

## Installation

You can install the package using pip:

```
pip install diz
```

## Usage

Here is a basic example of how to use the `Diz` class and the `LABVALUE` dataclass:

```python
import diz

# define patients
patients = [{'patid': 234234, 'startdatum':'2020-01-01', 'enddatum':'2020-01-03'},
            {'patid': 11111,  'startdatum':'2020-01-01', 'enddatum':'2020-01-03'},
            {'patid': 22222,  'startdatum':'2020-01-01', 'enddatum':'2020-01-03'},]

# initialize data access
data_access = diz.Diz(credentials='credentials.config')



# get lab values for each patient
for patient in patients:
    values = data_access.labvalues(patient_id= patient['patid'], start_date=patient['startdatum'], end_date=patient['enddatum'], type=diz.LABVALUE.Hb)
    
    patient['first_hb'] = values[0].value
    patient['first_hb_time'] = values[0].datetime

    # find lowest hb in values (super stupid implementation)
    hb = 100000000.0
    datetime = ""
    
    for value in values:
        if value.value < hb:
            hb = value.value
            datetime = value.datetime
            
    patient['lowest_hb'] = hb
    patient['lowest_hb_time'] = datetime
    
# print results
print(patients)

# now write list of dicts to csv
# csv.dictwriter(...)
```

## Testing

To run the tests for the `Diz` class, use the following command:

```
python -m unittest tests/test_diz.py
```

## Contributing

If you want to contribute to this project, please submit a pull request.

## License

This project is licensed under the MIT License.
```