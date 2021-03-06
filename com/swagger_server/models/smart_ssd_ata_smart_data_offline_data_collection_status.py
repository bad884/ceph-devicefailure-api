# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SmartSsdAtaSmartDataOfflineDataCollectionStatus(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, value: int=None, string: str=None):  # noqa: E501
        """SmartSsdAtaSmartDataOfflineDataCollectionStatus - a model defined in Swagger

        :param value: The value of this SmartSsdAtaSmartDataOfflineDataCollectionStatus.  # noqa: E501
        :type value: int
        :param string: The string of this SmartSsdAtaSmartDataOfflineDataCollectionStatus.  # noqa: E501
        :type string: str
        """
        self.swagger_types = {
            'value': int,
            'string': str
        }

        self.attribute_map = {
            'value': 'value',
            'string': 'string'
        }

        self._value = value
        self._string = string

    @classmethod
    def from_dict(cls, dikt) -> 'SmartSsdAtaSmartDataOfflineDataCollectionStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SmartSsd_ata_smart_data_offline_data_collection_status of this SmartSsdAtaSmartDataOfflineDataCollectionStatus.  # noqa: E501
        :rtype: SmartSsdAtaSmartDataOfflineDataCollectionStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> int:
        """Gets the value of this SmartSsdAtaSmartDataOfflineDataCollectionStatus.


        :return: The value of this SmartSsdAtaSmartDataOfflineDataCollectionStatus.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value: int):
        """Sets the value of this SmartSsdAtaSmartDataOfflineDataCollectionStatus.


        :param value: The value of this SmartSsdAtaSmartDataOfflineDataCollectionStatus.
        :type value: int
        """

        self._value = value

    @property
    def string(self) -> str:
        """Gets the string of this SmartSsdAtaSmartDataOfflineDataCollectionStatus.


        :return: The string of this SmartSsdAtaSmartDataOfflineDataCollectionStatus.
        :rtype: str
        """
        return self._string

    @string.setter
    def string(self, string: str):
        """Sets the string of this SmartSsdAtaSmartDataOfflineDataCollectionStatus.


        :param string: The string of this SmartSsdAtaSmartDataOfflineDataCollectionStatus.
        :type string: str
        """

        self._string = string
