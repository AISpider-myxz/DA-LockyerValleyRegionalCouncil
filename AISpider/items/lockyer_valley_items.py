from scrapy import Field
from . import BaseItem


class LockyerItem(BaseItem):
    application_id = Field()
    application_group = Field()
    application_type = Field()
    assessment_type = Field()
    lodgement_date = Field()
    description = Field()
    status = Field()
    decision = Field()
    finalised_date = Field()
    associated_name = Field()
    association = Field()
    address = Field()
    land_description = Field()
    documents = Field()

    class Meta:
        table = 'lockyer_valley'
        unique_fields = ['application_id',]