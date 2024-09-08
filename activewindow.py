from AppKit import NSWorkspace
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID


def get_active_window():
    active_win_name = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    window_list = CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly, kCGNullWindowID)
    for window in window_list:
        if 'kCGWindowOwnerName' in window and window['kCGWindowOwnerName'] == active_win_name and window.get('kCGWindowLayer', 0) == 0:
            if 'kCGWindowBounds' in window:
                bounds = window['kCGWindowBounds']
                x = bounds['X']
                y = bounds['Y']
                width = bounds['Width']
                height = bounds['Height']
                ret = ActiveWindow()
                ret.name = active_win_name
                ret.x = int(x)
                ret.y = int(y)
                ret.width = int(width)
                ret.height = int(height)
                ret.size = (ret.width, ret.height)
                ret.position = (ret.x, ret.y)
                return ret
    return None


class ActiveWindow:
    name = None
    x = None
    y = None
    width = None
    height = None
    size = None
    position = None
