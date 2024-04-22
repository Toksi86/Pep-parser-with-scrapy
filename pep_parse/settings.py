from .constants import PEP_PARSE

BOT_NAME = 'pep_parse'

SPIDER_MODULES = [PEP_PARSE]
NEWSPIDER_MODULE = PEP_PARSE

ROBOTSTXT_OBEY = True

FEED_EXPORT_ENCODING = "utf-8"
FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 500,
}
