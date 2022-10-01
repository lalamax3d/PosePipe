# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "PosePipe",
    "author": "ZonkoSoft, SpectralVectors, lalamax3d",
    "version": (0, 8, 5),
    "blender": (2, 80, 0),
    "location": "3D View > Sidebar > PosePipe",
    "description": "Motion capture using your camera!",
    "category": "3D View",
}

import bpy
from bpy.types import Panel, Operator, PropertyGroup, FloatProperty, PointerProperty
from bpy.utils import register_class, unregister_class
from bpy_extras.io_utils import ImportHelper
import time
import logging
import traceback
# from . OpenCVAnimOperator import state
from . PosePipe import Settings,PosePipePanel,RunOperator,RunFileSelector,SkeletonBuilder,RetimeAnimation

# # SPECIAL LINE
# bpy.types.Scene.ff_MC4B_prop_grp = bpy.props.PointerProperty(type=MC4BPropGrp)



# _classes = (

#     Settings,
#     PosePipePanel,
#     RunOperator,
#     RunFileSelector,
#     SkeletonBuilder,
#     RetimeAnimation,
# )

# register,unregister = bpy.utils.register_classes_factory(_classes)



_classes = [

    Settings,
    PosePipePanel,
    RunOperator,
    RunFileSelector,
    SkeletonBuilder,
    RetimeAnimation,
]
def register():
    for c in _classes: register_class(c)
    bpy.types.Scene.settings = bpy.props.PointerProperty(type=Settings)


def unregister():
    for c in _classes: unregister_class(c)
    del bpy.types.Scene.settings


if __name__ == "__main__":
    register()






