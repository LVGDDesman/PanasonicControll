#!/usr/bin/env python3
"""
Model for retrieval and adjustment of the cameraconfiguration and connection
"""

import requests
import xml.etree.ElementTree as ET
from model.commands.connection import Connection

class Settings():
    
    _instance = None
    settings = {}
    
    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.connection = Connection.instance()
        
        return cls._instance

    def get_setting(self, setting_type):
        if setting_type not in self.settings:
            return False
        return self.settings[setting_type]

    def set_setting(self, setting_type, value):
        self.settings[setting_type] = value
