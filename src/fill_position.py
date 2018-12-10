from std_msgs.msg import Float32
from interpreter_callback import CommandParent


class Command(CommandParent):
    def __init__(self, interpreter_info):
        CommandParent.__init__(self)
        self.val = 0.0


def process_key(val, cmd, interpreter_info):
    if val == 'BACK':
        if cmd != 0.0:
            cmd = max(min(-cmd / abs(cmd), 1.0), -1.0)
        elif val == 'STOP':
            cmd = 0.0
    else:
        cmd += val * interpreter_info['precision']

    # Bornage de -1 à 1
    cmd = max(min(cmd, 1.0), -1.0)

    return cmd


def fill_msg(cmd, interpreter_info):
    msg = Float32()
    min_cmd = float(interpreter_info['min'])
    max_cmd = float(interpreter_info['max'])
    range_cmd = max_cmd - min_cmd
    offset = range_cmd/2.0 + min_cmd

    msg.data = cmd.val * range_cmd + offset
    return msg
