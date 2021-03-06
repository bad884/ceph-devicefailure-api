# coding: utf-8

"""
    Ceph SMART Metrics

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SmartSsdAtaSmartDataSelfTestPollingMinutes(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'short': 'int',
        'extended': 'int',
        'conveyance': 'int'
    }

    attribute_map = {
        'short': 'short',
        'extended': 'extended',
        'conveyance': 'conveyance'
    }

    def __init__(self, short=None, extended=None, conveyance=None):  # noqa: E501
        """SmartSsdAtaSmartDataSelfTestPollingMinutes - a model defined in Swagger"""  # noqa: E501

        self._short = None
        self._extended = None
        self._conveyance = None
        self.discriminator = None

        if short is not None:
            self.short = short
        if extended is not None:
            self.extended = extended
        if conveyance is not None:
            self.conveyance = conveyance

    @property
    def short(self):
        """Gets the short of this SmartSsdAtaSmartDataSelfTestPollingMinutes.  # noqa: E501


        :return: The short of this SmartSsdAtaSmartDataSelfTestPollingMinutes.  # noqa: E501
        :rtype: int
        """
        return self._short

    @short.setter
    def short(self, short):
        """Sets the short of this SmartSsdAtaSmartDataSelfTestPollingMinutes.


        :param short: The short of this SmartSsdAtaSmartDataSelfTestPollingMinutes.  # noqa: E501
        :type: int
        """

        self._short = short

    @property
    def extended(self):
        """Gets the extended of this SmartSsdAtaSmartDataSelfTestPollingMinutes.  # noqa: E501


        :return: The extended of this SmartSsdAtaSmartDataSelfTestPollingMinutes.  # noqa: E501
        :rtype: int
        """
        return self._extended

    @extended.setter
    def extended(self, extended):
        """Sets the extended of this SmartSsdAtaSmartDataSelfTestPollingMinutes.


        :param extended: The extended of this SmartSsdAtaSmartDataSelfTestPollingMinutes.  # noqa: E501
        :type: int
        """

        self._extended = extended

    @property
    def conveyance(self):
        """Gets the conveyance of this SmartSsdAtaSmartDataSelfTestPollingMinutes.  # noqa: E501


        :return: The conveyance of this SmartSsdAtaSmartDataSelfTestPollingMinutes.  # noqa: E501
        :rtype: int
        """
        return self._conveyance

    @conveyance.setter
    def conveyance(self, conveyance):
        """Sets the conveyance of this SmartSsdAtaSmartDataSelfTestPollingMinutes.


        :param conveyance: The conveyance of this SmartSsdAtaSmartDataSelfTestPollingMinutes.  # noqa: E501
        :type: int
        """

        self._conveyance = conveyance

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SmartSsdAtaSmartDataSelfTestPollingMinutes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
