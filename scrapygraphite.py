'''Copyright 2011 Julien Duponchelle

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.'''

from scrapy.statscol import StatsCollector
from galena import Galena
from scrapy.conf import settings

class GraphiteStatsCollector(StatsCollector):
    def __init__(self):
        super(GraphiteStatsCollector, self).__init__()
        self._galena = Galena(host=settings['GRAPHITE_HOST'], port=settings['GRAPHITE_PORT'])

    def _get_stats_key(self, spider, key):
        if spider is not None:
            return "scrapy/spider/%s/%s" % (spider.name, key)
        return "scrapy/%s" % (key)

    def set_value(self, key, value, spider=None):
        super(GraphiteStatsCollector, self).set_value(key, value, spider)
        self._set_value(key, value, spider)

    def _set_value(self, key, value, spider):    
        if isinstance(value, int) or isinstance(value, float):
            if key == "envinfo/pid":
                return
            self._galena.send(self._get_stats_key(spider, key) + "_last", value)

    def inc_value(self, key, count=1, start=0, spider=None):
        super(GraphiteStatsCollector, self).inc_value(key, count, start, spider)
        self._galena.send(self._get_stats_key(spider, key) + "_sum", count)

    def max_value(self, key, value, spider=None):
        super(GraphiteStatsCollector, self).max_value(key, value, spider)
        self._galena.send(self._get_stats_key(spider, key) + "_max", value)

    def min_value(self, key, value, spider=None):
        super(GraphiteStatsCollector, self).min_value(key, value, spider)
        self._galena.send(self._get_stats_key(spider, key) + "_min", value)

    def set_stats(self, stats, spider=None):
        super(GraphiteStatsCollector, self).set_stats(stats, spider)
        for key in stats:
            self._set_value(key, stats[key],spider)
