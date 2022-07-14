from ConsumptionHour import ConsumptionHour
class Schedule:
    """ This object is used to provide a rate / KWH for any give hour """
    
    def get_rate(self, hour: ConsumptionHour) -> Rate:
        pass
    
class Rate:
    """ This object encompasses the rate information for a Schedule """
    
    def __init__(self, name: str, price_per_kwh: float) -> Rate:
        self.name = name
        self.price_per_kwh = price_per_kwh

    name: string
    price_per_kwh: float 
    