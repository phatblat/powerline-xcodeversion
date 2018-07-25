# vim:fileencoding=utf-8:noet

from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info
from subprocess import PIPE, Popen
import os, re, string


@requires_segment_info
class GitStatusSegment(Segment):

    def __call__(self, pl, segment_info, create_watcher):
        return 'xcv'
        # return [
        #     {'contents': 'xcv', 'highlight_groups': ['xcode_version', 'xcode_build'], 'divider_highlight_group': 'xcode_version:divider'}
        # ]


gitstatus = with_docstring(GitStatusSegment(),
'''Return the currently selected Xcode version.
''')
