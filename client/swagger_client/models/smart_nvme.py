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

from swagger_client.models.smart_nvme_device import SmartNvmeDevice  # noqa: F401,E501
from swagger_client.models.smart_nvme_local_time import SmartNvmeLocalTime  # noqa: F401,E501
from swagger_client.models.smart_nvme_nvme_namespaces import SmartNvmeNvmeNamespaces  # noqa: F401,E501
from swagger_client.models.smart_nvme_nvme_pci_vendor import SmartNvmeNvmePciVendor  # noqa: F401,E501
from swagger_client.models.smart_nvme_nvme_smart_health_information_log import SmartNvmeNvmeSmartHealthInformationLog  # noqa: F401,E501
from swagger_client.models.smart_nvme_power_on_time import SmartNvmePowerOnTime  # noqa: F401,E501
from swagger_client.models.smart_nvme_size import SmartNvmeSize  # noqa: F401,E501
from swagger_client.models.smart_nvme_smart_status import SmartNvmeSmartStatus  # noqa: F401,E501
from swagger_client.models.smart_nvme_smartctl import SmartNvmeSmartctl  # noqa: F401,E501
from swagger_client.models.smart_nvme_temperature import SmartNvmeTemperature  # noqa: F401,E501


class SmartNvme(object):
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
        'json_format_version': 'list[int]',
        'smartctl': 'SmartNvmeSmartctl',
        'device': 'SmartNvmeDevice',
        'model_name': 'str',
        'serial_number': 'str',
        'firmware_version': 'str',
        'nvme_pci_vendor': 'SmartNvmeNvmePciVendor',
        'nvme_ieee_oui_identifier': 'int',
        'nvme_controller_id': 'int',
        'nvme_number_of_namespaces': 'int',
        'nvme_namespaces': 'list[SmartNvmeNvmeNamespaces]',
        'user_capacity': 'SmartNvmeSize',
        'logical_block_size': 'int',
        'local_time': 'SmartNvmeLocalTime',
        'smart_status': 'SmartNvmeSmartStatus',
        'nvme_smart_health_information_log': 'SmartNvmeNvmeSmartHealthInformationLog',
        'temperature': 'SmartNvmeTemperature',
        'power_cycle_count': 'int',
        'power_on_time': 'SmartNvmePowerOnTime'
    }

    attribute_map = {
        'json_format_version': 'json_format_version',
        'smartctl': 'smartctl',
        'device': 'device',
        'model_name': 'model_name',
        'serial_number': 'serial_number',
        'firmware_version': 'firmware_version',
        'nvme_pci_vendor': 'nvme_pci_vendor',
        'nvme_ieee_oui_identifier': 'nvme_ieee_oui_identifier',
        'nvme_controller_id': 'nvme_controller_id',
        'nvme_number_of_namespaces': 'nvme_number_of_namespaces',
        'nvme_namespaces': 'nvme_namespaces',
        'user_capacity': 'user_capacity',
        'logical_block_size': 'logical_block_size',
        'local_time': 'local_time',
        'smart_status': 'smart_status',
        'nvme_smart_health_information_log': 'nvme_smart_health_information_log',
        'temperature': 'temperature',
        'power_cycle_count': 'power_cycle_count',
        'power_on_time': 'power_on_time'
    }

    def __init__(self, json_format_version=None, smartctl=None, device=None, model_name=None, serial_number=None, firmware_version=None, nvme_pci_vendor=None, nvme_ieee_oui_identifier=None, nvme_controller_id=None, nvme_number_of_namespaces=None, nvme_namespaces=None, user_capacity=None, logical_block_size=None, local_time=None, smart_status=None, nvme_smart_health_information_log=None, temperature=None, power_cycle_count=None, power_on_time=None):  # noqa: E501
        """SmartNvme - a model defined in Swagger"""  # noqa: E501

        self._json_format_version = None
        self._smartctl = None
        self._device = None
        self._model_name = None
        self._serial_number = None
        self._firmware_version = None
        self._nvme_pci_vendor = None
        self._nvme_ieee_oui_identifier = None
        self._nvme_controller_id = None
        self._nvme_number_of_namespaces = None
        self._nvme_namespaces = None
        self._user_capacity = None
        self._logical_block_size = None
        self._local_time = None
        self._smart_status = None
        self._nvme_smart_health_information_log = None
        self._temperature = None
        self._power_cycle_count = None
        self._power_on_time = None
        self.discriminator = None

        if json_format_version is not None:
            self.json_format_version = json_format_version
        if smartctl is not None:
            self.smartctl = smartctl
        if device is not None:
            self.device = device
        if model_name is not None:
            self.model_name = model_name
        if serial_number is not None:
            self.serial_number = serial_number
        if firmware_version is not None:
            self.firmware_version = firmware_version
        if nvme_pci_vendor is not None:
            self.nvme_pci_vendor = nvme_pci_vendor
        if nvme_ieee_oui_identifier is not None:
            self.nvme_ieee_oui_identifier = nvme_ieee_oui_identifier
        if nvme_controller_id is not None:
            self.nvme_controller_id = nvme_controller_id
        if nvme_number_of_namespaces is not None:
            self.nvme_number_of_namespaces = nvme_number_of_namespaces
        if nvme_namespaces is not None:
            self.nvme_namespaces = nvme_namespaces
        if user_capacity is not None:
            self.user_capacity = user_capacity
        if logical_block_size is not None:
            self.logical_block_size = logical_block_size
        if local_time is not None:
            self.local_time = local_time
        if smart_status is not None:
            self.smart_status = smart_status
        if nvme_smart_health_information_log is not None:
            self.nvme_smart_health_information_log = nvme_smart_health_information_log
        if temperature is not None:
            self.temperature = temperature
        if power_cycle_count is not None:
            self.power_cycle_count = power_cycle_count
        if power_on_time is not None:
            self.power_on_time = power_on_time

    @property
    def json_format_version(self):
        """Gets the json_format_version of this SmartNvme.  # noqa: E501


        :return: The json_format_version of this SmartNvme.  # noqa: E501
        :rtype: list[int]
        """
        return self._json_format_version

    @json_format_version.setter
    def json_format_version(self, json_format_version):
        """Sets the json_format_version of this SmartNvme.


        :param json_format_version: The json_format_version of this SmartNvme.  # noqa: E501
        :type: list[int]
        """

        self._json_format_version = json_format_version

    @property
    def smartctl(self):
        """Gets the smartctl of this SmartNvme.  # noqa: E501


        :return: The smartctl of this SmartNvme.  # noqa: E501
        :rtype: SmartNvmeSmartctl
        """
        return self._smartctl

    @smartctl.setter
    def smartctl(self, smartctl):
        """Sets the smartctl of this SmartNvme.


        :param smartctl: The smartctl of this SmartNvme.  # noqa: E501
        :type: SmartNvmeSmartctl
        """

        self._smartctl = smartctl

    @property
    def device(self):
        """Gets the device of this SmartNvme.  # noqa: E501


        :return: The device of this SmartNvme.  # noqa: E501
        :rtype: SmartNvmeDevice
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this SmartNvme.


        :param device: The device of this SmartNvme.  # noqa: E501
        :type: SmartNvmeDevice
        """

        self._device = device

    @property
    def model_name(self):
        """Gets the model_name of this SmartNvme.  # noqa: E501


        :return: The model_name of this SmartNvme.  # noqa: E501
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this SmartNvme.


        :param model_name: The model_name of this SmartNvme.  # noqa: E501
        :type: str
        """

        self._model_name = model_name

    @property
    def serial_number(self):
        """Gets the serial_number of this SmartNvme.  # noqa: E501


        :return: The serial_number of this SmartNvme.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this SmartNvme.


        :param serial_number: The serial_number of this SmartNvme.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def firmware_version(self):
        """Gets the firmware_version of this SmartNvme.  # noqa: E501


        :return: The firmware_version of this SmartNvme.  # noqa: E501
        :rtype: str
        """
        return self._firmware_version

    @firmware_version.setter
    def firmware_version(self, firmware_version):
        """Sets the firmware_version of this SmartNvme.


        :param firmware_version: The firmware_version of this SmartNvme.  # noqa: E501
        :type: str
        """

        self._firmware_version = firmware_version

    @property
    def nvme_pci_vendor(self):
        """Gets the nvme_pci_vendor of this SmartNvme.  # noqa: E501


        :return: The nvme_pci_vendor of this SmartNvme.  # noqa: E501
        :rtype: SmartNvmeNvmePciVendor
        """
        return self._nvme_pci_vendor

    @nvme_pci_vendor.setter
    def nvme_pci_vendor(self, nvme_pci_vendor):
        """Sets the nvme_pci_vendor of this SmartNvme.


        :param nvme_pci_vendor: The nvme_pci_vendor of this SmartNvme.  # noqa: E501
        :type: SmartNvmeNvmePciVendor
        """

        self._nvme_pci_vendor = nvme_pci_vendor

    @property
    def nvme_ieee_oui_identifier(self):
        """Gets the nvme_ieee_oui_identifier of this SmartNvme.  # noqa: E501


        :return: The nvme_ieee_oui_identifier of this SmartNvme.  # noqa: E501
        :rtype: int
        """
        return self._nvme_ieee_oui_identifier

    @nvme_ieee_oui_identifier.setter
    def nvme_ieee_oui_identifier(self, nvme_ieee_oui_identifier):
        """Sets the nvme_ieee_oui_identifier of this SmartNvme.


        :param nvme_ieee_oui_identifier: The nvme_ieee_oui_identifier of this SmartNvme.  # noqa: E501
        :type: int
        """

        self._nvme_ieee_oui_identifier = nvme_ieee_oui_identifier

    @property
    def nvme_controller_id(self):
        """Gets the nvme_controller_id of this SmartNvme.  # noqa: E501


        :return: The nvme_controller_id of this SmartNvme.  # noqa: E501
        :rtype: int
        """
        return self._nvme_controller_id

    @nvme_controller_id.setter
    def nvme_controller_id(self, nvme_controller_id):
        """Sets the nvme_controller_id of this SmartNvme.


        :param nvme_controller_id: The nvme_controller_id of this SmartNvme.  # noqa: E501
        :type: int
        """

        self._nvme_controller_id = nvme_controller_id

    @property
    def nvme_number_of_namespaces(self):
        """Gets the nvme_number_of_namespaces of this SmartNvme.  # noqa: E501


        :return: The nvme_number_of_namespaces of this SmartNvme.  # noqa: E501
        :rtype: int
        """
        return self._nvme_number_of_namespaces

    @nvme_number_of_namespaces.setter
    def nvme_number_of_namespaces(self, nvme_number_of_namespaces):
        """Sets the nvme_number_of_namespaces of this SmartNvme.


        :param nvme_number_of_namespaces: The nvme_number_of_namespaces of this SmartNvme.  # noqa: E501
        :type: int
        """

        self._nvme_number_of_namespaces = nvme_number_of_namespaces

    @property
    def nvme_namespaces(self):
        """Gets the nvme_namespaces of this SmartNvme.  # noqa: E501


        :return: The nvme_namespaces of this SmartNvme.  # noqa: E501
        :rtype: list[SmartNvmeNvmeNamespaces]
        """
        return self._nvme_namespaces

    @nvme_namespaces.setter
    def nvme_namespaces(self, nvme_namespaces):
        """Sets the nvme_namespaces of this SmartNvme.


        :param nvme_namespaces: The nvme_namespaces of this SmartNvme.  # noqa: E501
        :type: list[SmartNvmeNvmeNamespaces]
        """

        self._nvme_namespaces = nvme_namespaces

    @property
    def user_capacity(self):
        """Gets the user_capacity of this SmartNvme.  # noqa: E501


        :return: The user_capacity of this SmartNvme.  # noqa: E501
        :rtype: SmartNvmeSize
        """
        return self._user_capacity

    @user_capacity.setter
    def user_capacity(self, user_capacity):
        """Sets the user_capacity of this SmartNvme.


        :param user_capacity: The user_capacity of this SmartNvme.  # noqa: E501
        :type: SmartNvmeSize
        """

        self._user_capacity = user_capacity

    @property
    def logical_block_size(self):
        """Gets the logical_block_size of this SmartNvme.  # noqa: E501


        :return: The logical_block_size of this SmartNvme.  # noqa: E501
        :rtype: int
        """
        return self._logical_block_size

    @logical_block_size.setter
    def logical_block_size(self, logical_block_size):
        """Sets the logical_block_size of this SmartNvme.


        :param logical_block_size: The logical_block_size of this SmartNvme.  # noqa: E501
        :type: int
        """

        self._logical_block_size = logical_block_size

    @property
    def local_time(self):
        """Gets the local_time of this SmartNvme.  # noqa: E501


        :return: The local_time of this SmartNvme.  # noqa: E501
        :rtype: SmartNvmeLocalTime
        """
        return self._local_time

    @local_time.setter
    def local_time(self, local_time):
        """Sets the local_time of this SmartNvme.


        :param local_time: The local_time of this SmartNvme.  # noqa: E501
        :type: SmartNvmeLocalTime
        """

        self._local_time = local_time

    @property
    def smart_status(self):
        """Gets the smart_status of this SmartNvme.  # noqa: E501


        :return: The smart_status of this SmartNvme.  # noqa: E501
        :rtype: SmartNvmeSmartStatus
        """
        return self._smart_status

    @smart_status.setter
    def smart_status(self, smart_status):
        """Sets the smart_status of this SmartNvme.


        :param smart_status: The smart_status of this SmartNvme.  # noqa: E501
        :type: SmartNvmeSmartStatus
        """

        self._smart_status = smart_status

    @property
    def nvme_smart_health_information_log(self):
        """Gets the nvme_smart_health_information_log of this SmartNvme.  # noqa: E501


        :return: The nvme_smart_health_information_log of this SmartNvme.  # noqa: E501
        :rtype: SmartNvmeNvmeSmartHealthInformationLog
        """
        return self._nvme_smart_health_information_log

    @nvme_smart_health_information_log.setter
    def nvme_smart_health_information_log(self, nvme_smart_health_information_log):
        """Sets the nvme_smart_health_information_log of this SmartNvme.


        :param nvme_smart_health_information_log: The nvme_smart_health_information_log of this SmartNvme.  # noqa: E501
        :type: SmartNvmeNvmeSmartHealthInformationLog
        """

        self._nvme_smart_health_information_log = nvme_smart_health_information_log

    @property
    def temperature(self):
        """Gets the temperature of this SmartNvme.  # noqa: E501


        :return: The temperature of this SmartNvme.  # noqa: E501
        :rtype: SmartNvmeTemperature
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this SmartNvme.


        :param temperature: The temperature of this SmartNvme.  # noqa: E501
        :type: SmartNvmeTemperature
        """

        self._temperature = temperature

    @property
    def power_cycle_count(self):
        """Gets the power_cycle_count of this SmartNvme.  # noqa: E501


        :return: The power_cycle_count of this SmartNvme.  # noqa: E501
        :rtype: int
        """
        return self._power_cycle_count

    @power_cycle_count.setter
    def power_cycle_count(self, power_cycle_count):
        """Sets the power_cycle_count of this SmartNvme.


        :param power_cycle_count: The power_cycle_count of this SmartNvme.  # noqa: E501
        :type: int
        """

        self._power_cycle_count = power_cycle_count

    @property
    def power_on_time(self):
        """Gets the power_on_time of this SmartNvme.  # noqa: E501


        :return: The power_on_time of this SmartNvme.  # noqa: E501
        :rtype: SmartNvmePowerOnTime
        """
        return self._power_on_time

    @power_on_time.setter
    def power_on_time(self, power_on_time):
        """Sets the power_on_time of this SmartNvme.


        :param power_on_time: The power_on_time of this SmartNvme.  # noqa: E501
        :type: SmartNvmePowerOnTime
        """

        self._power_on_time = power_on_time

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
        if not isinstance(other, SmartNvme):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
