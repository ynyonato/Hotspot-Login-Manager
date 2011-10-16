# -*- coding:utf-8 -*-
#
# hotspot-login-manager
# https://github.com/syam44/Hotspot-Login-Manager
#
# Distributed under the GNU General Public License version 3
# https://www.gnu.org/copyleft/gpl.html
#
# Authors: syam (aks92@free.fr)
#
# Description: Handles platform-specific implementations.
#


#-----------------------------------------------------------------------------
import os
import platform
import sys
import types
#
import hotspot_login_manager.libs.hlm_i18n
_, _N = hotspot_login_manager.libs.hlm_i18n.translators()

#-----------------------------------------------------------------------------
#
# Detect the current platform, and exits if it is not supported.
#
__platform = None

if (os.name == 'posix') and (platform.system() == 'Linux'):
  __platform = 'linux'

else:
  print(_('Sorry, your platform ({0}/{1} {2}) is not yet supported.').format(os.name, platform.system(), platform.release()))
  sys.exit(255)


#-----------------------------------------------------------------------------
#
# Load platform-specific modules
#
hlmp_network = None


if __platform == 'linux':
    # hlmp_network
    import hotspot_login_manager.libs.linux.hlmp_network
    hlmp_network = hotspot_login_manager.libs.linux.hlmp_network


#-----------------------------------------------------------------------------
def install(wrapperVars, importModule):
    ''' Install every public variable/function/class defined in importModule
        into the wrapper module.
        Modules are not installed.

        Public items are the ones NOT starting with a double underscore.

        Usage:
            from hotspot_login_manager.libs import hlm_platform
            hlm_platform.install(vars(), hlm_platform.hlmp_module)
    '''
    moduleVars = vars(importModule)
    for varName in moduleVars.keys():
        varObject = moduleVars[varName]
        if (not type(varObject) is types.ModuleType) and (not varName.startswith('__')):
            wrapperVars[varName] = varObject


#-----------------------------------------------------------------------------
def getPlatform():
    ''' Return the current platform.

        Currently supported:
            linux
    '''
    return __platform


#-----------------------------------------------------------------------------
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
