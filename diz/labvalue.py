from dataclasses import dataclass

@dataclass(frozen=True)
class LABVALUE:
    """ Constants for accessing lab values 
    """
    Hb: str = "Hb"
    Hkt: str = "Hkt"
    WBC: str = "WBC"
    Haemaglobin: str = Hb
    Haematokrit: str = Hkt
    Leukocytes: str = WBC
    
    # TODO: add more lab values