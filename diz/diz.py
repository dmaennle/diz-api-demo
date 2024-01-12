from .labvalue import LABVALUE
from collections import namedtuple

class Diz:
    """ Class for accessing the UMM DIZ data API for quickly handling data requests.
    """
    
    def __init__(self, credentials: str):
        """Initialize Diz class

        Args:
            credentials (str): path to credentials file
        """
        # TODO read credentials and connect to API
        pass
    
    def labvalues(self, patient_id: int, start_date: str, end_date: str, type: str) -> namedtuple:
        """Get lab values for a patient between two dates

        Args:
            patient_id (int): Patient ID
            start_date (str): Start date of query
            end_date (str): End date of query
            type (str): Labvalue to get

        Returns:
            namedtuple: tuple of labvalues with value and datetime as fields.
        """
        
        # TODO: implement this method
        
        # Some Demo code to show how to return a namedtuple:
        LabValue = namedtuple('LabValue', ['value', 'datetime'])
        
        return_values = []
        
        if type == LABVALUE.Hb:
            # some dummy values           
            return_values.append(LabValue(11.87, "2020-01-01"))
            return_values.append(LabValue(12.12, "2020-01-02"))
            return_values.append(LabValue(8.12, "2020-01-03"))
            return return_values
        
        return None
              
    # Add further methods here