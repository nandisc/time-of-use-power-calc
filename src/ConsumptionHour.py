from Rates import Schedule

class ConsumptionHour:

    @staticmethod
    def from_csv(self, raw_row: str) -> ConsumptionHour:
        pass

    
    def get_rate(self, schedule: Schedule) -> UseRate:
        """ Return the rate for this hour based on the Schedule """
        pass
    
    def get_cost(self) -> float:
        """ The cost for the power consumed by this hour """
        pass

    