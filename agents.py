from parlai.core.teachers import ParlAIDialogTeacher
import copy

class DefaultTeacher(ParlAIDialogTeacher):
    def __init__(self, opt, shared=None):
        opt = copy.deepcopy(opt)

        # get datafile
        opt['parlaidialogteacher_datafile'] = "parlai/tasks/kossie/data.txt"

        super().__init__(opt, shared)