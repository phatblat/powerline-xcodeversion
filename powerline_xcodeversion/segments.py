# vim:fileencoding=utf-8:noet
# -*- coding: UTF-8 -*-

from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info
from subprocess import PIPE, Popen, call, check_output, CalledProcessError
import os, re, string


#@requires_segment_info
class XcodeVersionSegment(Segment):

    def __call__(self, pl): #, segment_info): #, create_watcher):
        # pl.warn("I can haz log?")
        version = self.marketing_version(pl)
        return [{
            'contents': version,
            'highlight_groups': ['xcode_version', 'xcode_build'],
            'divider_highlight_group': 'xcode_version:divider',
        }]

    def marketing_version(self, pl):
        command = ( "plutil -p $(xcode-select -p)/../version.plist"
                    " | grep -e CFBundleShortVersionString"
                    " | sed 's/[^0-9\.]*//g'"
                    )
        pl.debug("command: " + command)
        output = self.execute(pl, command)

        return "🛠️ " + output

    # command is string array
    def execute(self, pl, command):
        pl.debug('Executing command: %s' % ' '.join(command))

        try:
            output = check_output(command, shell=True).decode('utf-8').rstrip()
            pl.debug("output: " + output)
        except CalledProcessError as e:
            pl.error("ERROR " + e.returncode + ": " + e.output)
            return

        return output

xcodeversion = with_docstring(XcodeVersionSegment(),
'''Returns the currently selected Xcode version.
''')
