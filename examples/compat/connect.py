#!/usr/bin/env python3
from synack.compat.v1 import synack
import sys

s1 = synack()
s1.headless = False
s1.configFile = "~/.synack/synack.conf"
s1.connectToPlatform()
s1.getSessionToken()
