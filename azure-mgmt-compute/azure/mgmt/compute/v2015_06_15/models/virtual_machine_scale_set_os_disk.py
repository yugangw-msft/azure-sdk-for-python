# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualMachineScaleSetOSDisk(Model):
    """Describes a virtual machine scale set operating system disk.

    :param name: The disk name.
    :type name: str
    :param caching: Specifies the caching requirements. <br><br> Possible
     values are: <br><br> **None** <br><br> **ReadOnly** <br><br> **ReadWrite**
     <br><br> Default: **None for Standard storage. ReadOnly for Premium
     storage**. Possible values include: 'None', 'ReadOnly', 'ReadWrite'
    :type caching: str or ~azure.mgmt.compute.v2015_06_15.models.CachingTypes
    :param create_option: Specifies how the virtual machines in the scale set
     should be created.<br><br> The only allowed value is: **FromImage**
     \\u2013 This value is used when you are using an image to create the
     virtual machine. If you are using a platform image, you also use the
     imageReference element described above. If you are using a marketplace
     image, you  also use the plan element previously described. Possible
     values include: 'FromImage', 'Empty', 'Attach'
    :type create_option: str or
     ~azure.mgmt.compute.v2015_06_15.models.DiskCreateOptionTypes
    :param os_type: This property allows you to specify the type of the OS
     that is included in the disk if creating a VM from user-image or a
     specialized VHD. <br><br> Possible values are: <br><br> **Windows**
     <br><br> **Linux**. Possible values include: 'Windows', 'Linux'
    :type os_type: str or
     ~azure.mgmt.compute.v2015_06_15.models.OperatingSystemTypes
    :param image: The Source User Image VirtualHardDisk. This VirtualHardDisk
     will be copied before using it to attach to the Virtual Machine. If
     SourceImage is provided, the destination VirtualHardDisk should not exist.
    :type image: ~azure.mgmt.compute.v2015_06_15.models.VirtualHardDisk
    :param vhd_containers: The list of virtual hard disk container uris.
    :type vhd_containers: list[str]
    """

    _validation = {
        'name': {'required': True},
        'create_option': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'caching': {'key': 'caching', 'type': 'CachingTypes'},
        'create_option': {'key': 'createOption', 'type': 'DiskCreateOptionTypes'},
        'os_type': {'key': 'osType', 'type': 'OperatingSystemTypes'},
        'image': {'key': 'image', 'type': 'VirtualHardDisk'},
        'vhd_containers': {'key': 'vhdContainers', 'type': '[str]'},
    }

    def __init__(self, name, create_option, caching=None, os_type=None, image=None, vhd_containers=None):
        self.name = name
        self.caching = caching
        self.create_option = create_option
        self.os_type = os_type
        self.image = image
        self.vhd_containers = vhd_containers
