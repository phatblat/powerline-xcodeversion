# vim:fileencoding=utf-8:noet

from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info
from subprocess import PIPE, Popen
import os, re, string


#@requires_segment_info
class XcodeVersionSegment(Segment):

    def __call__(self, pl): #, segment_info): #, create_watcher):
        pl.warn("I can haz log?")
        return [{
            'contents': 'xcv',
            'highlight_groups': ['xcode_version', 'xcode_build'],
        }]
        # return [
        #     {'contents': 'xcv', 'highlight_groups': ['xcode_version', 'xcode_build'], 'divider_highlight_group': 'xcode_version:divider'}
        # ]


xcodeversion = with_docstring(XcodeVersionSegment(),
'''Returns the currently selected Xcode version.
''')
