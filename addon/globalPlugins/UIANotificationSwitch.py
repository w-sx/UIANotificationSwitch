import addonHandler
import config
import globalPluginHandler
from scriptHandler import script
import tones
import ui

addonHandler.initTranslation()

config.conf.spec['UIANotificationSwitch'] = {"switch": "integer(default=0)"}

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = _("UIANotificationSwitch")

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.status = [_('off'),_('on'),_('beep')]

	def event_UIA_notification(self, obj, nextHandler):
		switch = int(config.conf['UIANotificationSwitch']['switch'])
		if switch == 0: nextHandler()
		elif switch > 0: tones.beep(440,10)
		elif switch: return

	@script(
		description=_('switch UIA Notification'),
		gesture='kb:NVDA+I'
	)
	def script_UIANotificationSwitch(self, gesture):
		switch = int(config.conf['UIANotificationSwitch']['switch']) + 1
		if switch>1: switch = -1
		config.conf['UIANotificationSwitch']['switch'] = switch
		ui.message(_('UIA Notification ') + self.status[switch + 1])
