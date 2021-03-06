# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.smart_ssd_ata_sct_temperature_history_temperature import SmartSsdAtaSctTemperatureHistoryTemperature  # noqa: F401,E501
from swagger_server import util


class SmartSsdAtaSctTemperatureHistory(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, version: int=None, sampling_period_minutes: int=None, logging_interval_minutes: int=None, temperature: SmartSsdAtaSctTemperatureHistoryTemperature=None, size: int=None, index: int=None, table: List[int]=None):  # noqa: E501
        """SmartSsdAtaSctTemperatureHistory - a model defined in Swagger

        :param version: The version of this SmartSsdAtaSctTemperatureHistory.  # noqa: E501
        :type version: int
        :param sampling_period_minutes: The sampling_period_minutes of this SmartSsdAtaSctTemperatureHistory.  # noqa: E501
        :type sampling_period_minutes: int
        :param logging_interval_minutes: The logging_interval_minutes of this SmartSsdAtaSctTemperatureHistory.  # noqa: E501
        :type logging_interval_minutes: int
        :param temperature: The temperature of this SmartSsdAtaSctTemperatureHistory.  # noqa: E501
        :type temperature: SmartSsdAtaSctTemperatureHistoryTemperature
        :param size: The size of this SmartSsdAtaSctTemperatureHistory.  # noqa: E501
        :type size: int
        :param index: The index of this SmartSsdAtaSctTemperatureHistory.  # noqa: E501
        :type index: int
        :param table: The table of this SmartSsdAtaSctTemperatureHistory.  # noqa: E501
        :type table: List[int]
        """
        self.swagger_types = {
            'version': int,
            'sampling_period_minutes': int,
            'logging_interval_minutes': int,
            'temperature': SmartSsdAtaSctTemperatureHistoryTemperature,
            'size': int,
            'index': int,
            'table': List[int]
        }

        self.attribute_map = {
            'version': 'version',
            'sampling_period_minutes': 'sampling_period_minutes',
            'logging_interval_minutes': 'logging_interval_minutes',
            'temperature': 'temperature',
            'size': 'size',
            'index': 'index',
            'table': 'table'
        }

        self._version = version
        self._sampling_period_minutes = sampling_period_minutes
        self._logging_interval_minutes = logging_interval_minutes
        self._temperature = temperature
        self._size = size
        self._index = index
        self._table = table

    @classmethod
    def from_dict(cls, dikt) -> 'SmartSsdAtaSctTemperatureHistory':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SmartSsd_ata_sct_temperature_history of this SmartSsdAtaSctTemperatureHistory.  # noqa: E501
        :rtype: SmartSsdAtaSctTemperatureHistory
        """
        return util.deserialize_model(dikt, cls)

    @property
    def version(self) -> int:
        """Gets the version of this SmartSsdAtaSctTemperatureHistory.


        :return: The version of this SmartSsdAtaSctTemperatureHistory.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int):
        """Sets the version of this SmartSsdAtaSctTemperatureHistory.


        :param version: The version of this SmartSsdAtaSctTemperatureHistory.
        :type version: int
        """

        self._version = version

    @property
    def sampling_period_minutes(self) -> int:
        """Gets the sampling_period_minutes of this SmartSsdAtaSctTemperatureHistory.


        :return: The sampling_period_minutes of this SmartSsdAtaSctTemperatureHistory.
        :rtype: int
        """
        return self._sampling_period_minutes

    @sampling_period_minutes.setter
    def sampling_period_minutes(self, sampling_period_minutes: int):
        """Sets the sampling_period_minutes of this SmartSsdAtaSctTemperatureHistory.


        :param sampling_period_minutes: The sampling_period_minutes of this SmartSsdAtaSctTemperatureHistory.
        :type sampling_period_minutes: int
        """

        self._sampling_period_minutes = sampling_period_minutes

    @property
    def logging_interval_minutes(self) -> int:
        """Gets the logging_interval_minutes of this SmartSsdAtaSctTemperatureHistory.


        :return: The logging_interval_minutes of this SmartSsdAtaSctTemperatureHistory.
        :rtype: int
        """
        return self._logging_interval_minutes

    @logging_interval_minutes.setter
    def logging_interval_minutes(self, logging_interval_minutes: int):
        """Sets the logging_interval_minutes of this SmartSsdAtaSctTemperatureHistory.


        :param logging_interval_minutes: The logging_interval_minutes of this SmartSsdAtaSctTemperatureHistory.
        :type logging_interval_minutes: int
        """

        self._logging_interval_minutes = logging_interval_minutes

    @property
    def temperature(self) -> SmartSsdAtaSctTemperatureHistoryTemperature:
        """Gets the temperature of this SmartSsdAtaSctTemperatureHistory.


        :return: The temperature of this SmartSsdAtaSctTemperatureHistory.
        :rtype: SmartSsdAtaSctTemperatureHistoryTemperature
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature: SmartSsdAtaSctTemperatureHistoryTemperature):
        """Sets the temperature of this SmartSsdAtaSctTemperatureHistory.


        :param temperature: The temperature of this SmartSsdAtaSctTemperatureHistory.
        :type temperature: SmartSsdAtaSctTemperatureHistoryTemperature
        """

        self._temperature = temperature

    @property
    def size(self) -> int:
        """Gets the size of this SmartSsdAtaSctTemperatureHistory.


        :return: The size of this SmartSsdAtaSctTemperatureHistory.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size: int):
        """Sets the size of this SmartSsdAtaSctTemperatureHistory.


        :param size: The size of this SmartSsdAtaSctTemperatureHistory.
        :type size: int
        """

        self._size = size

    @property
    def index(self) -> int:
        """Gets the index of this SmartSsdAtaSctTemperatureHistory.


        :return: The index of this SmartSsdAtaSctTemperatureHistory.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index: int):
        """Sets the index of this SmartSsdAtaSctTemperatureHistory.


        :param index: The index of this SmartSsdAtaSctTemperatureHistory.
        :type index: int
        """

        self._index = index

    @property
    def table(self) -> List[int]:
        """Gets the table of this SmartSsdAtaSctTemperatureHistory.


        :return: The table of this SmartSsdAtaSctTemperatureHistory.
        :rtype: List[int]
        """
        return self._table

    @table.setter
    def table(self, table: List[int]):
        """Sets the table of this SmartSsdAtaSctTemperatureHistory.


        :param table: The table of this SmartSsdAtaSctTemperatureHistory.
        :type table: List[int]
        """

        self._table = table
