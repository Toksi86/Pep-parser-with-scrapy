import csv
import datetime as dt

from pep_parse.constants import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    total = 0
    status_list = {}

    def open_spider(self, spider):
        self.total = 0
        self.status_list = {}

    def process_item(self, item, spider):
        self.status_list[item['status']] = self.status_list.get(
            item['status'], 0) + 1
        self.total += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)

        time_now = dt.datetime.strftime(dt.datetime.now(), DATETIME_FORMAT)
        file_name = f'status_summary_{time_now}.csv'
        file_path = results_dir / file_name

        with open(file_path, mode='w', encoding='utf-8') as f:
            fieldnames = ['Статус', 'Количество']
            writer = csv.DictWriter(f,
                                    fieldnames=fieldnames,
                                    dialect='unix',
                                    quoting=csv.QUOTE_NONE
                                    )
            writer.writeheader()
            for status, count in self.status_list.items():
                writer.writerow({'Статус': status,
                                 'Количество': count})
            writer.writerow({'Статус': 'Total',
                             'Количество': sum(self.status_list.values())
                             })
