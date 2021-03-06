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


class SmartNvmeLocalTime(object):
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
        'time_t': 'int',
        'asctime': 'str'
    }

    attribute_map = {
        'time_t': 'time_t',
        'asctime': 'asctime'
    }

    def __init__(self, time_t=None, asctime=None):  # noqa: E501
        """SmartNvmeLocalTime - a model defined in Swagger"""  # noqa: E501

        self._time_t = None
        self._asctime = None
        self.discriminator = None

        if time_t is not None:
            self.time_t = time_t
        if asctime is not None:
            self.asctime = asctime

    @property
    def time_t(self):
        """Gets the time_t of this SmartNvmeLocalTime.  # noqa: E501


        :return: The time_t of this SmartNvmeLocalTime.  # noqa: E501
        :rtype: int
        """
        return self._time_t

    @time_t.setter
    def time_t(self, time_t):
        """Sets the time_t of this SmartNvmeLocalTime.


        :param time_t: The time_t of this SmartNvmeLocalTime.  # noqa: E501
        :type: int
        """

        self._time_t = time_t

    @property
    def asctime(self):
        """Gets the asctime of this SmartNvmeLocalTime.  # noqa: E501


        :return: The asctime of this SmartNvmeLocalTime.  # noqa: E501
        :rtype: str
        """
        return self._asctime

    @asctime.setter
    def asctime(self, asctime):
        """Sets the asctime of this SmartNvmeLocalTime.


        :param asctime: The asctime of this SmartNvmeLocalTime.  # noqa: E501
        :type: str
        """

        self._asctime = asctime

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
        if not isinstance(other, SmartNvmeLocalTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
