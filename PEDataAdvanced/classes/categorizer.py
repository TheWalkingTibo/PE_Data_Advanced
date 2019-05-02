class Categorizer(object):
    format = '%d/%m/%Y'

    @staticmethod
    def get_month_category(month_digits):
        month = int(month_digits);

        if month < 4:
            return 1
        elif month < 7:
            return 2
        elif month < 10:
            return 3
        else:
            return 4

    @staticmethod
    def get_engagement_for_category(engagement_category):
        if engagement_category == 1:
            return "zeer goed"
        elif engagement_category == 2 or engagement_category == 3:
            return "goed"
        elif engagement_category == 4:
            return "matig"
