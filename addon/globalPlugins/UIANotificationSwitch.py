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
		self.switch = config.conf['UIANotificationSwitch']['switch']
		self.description = [_('UIA Notification off'),_('UIA Notification on'),_('UIA notification beep')]

	def event_UIA_notification(self, obj, nextHandler):
		if self.switch == 0: nextHandler()
		elif self.switch > 0: tones.beep(440,10)
		elif self.switch: return

	@script(
		description=_('switch UIA Notification'),
		gesture='kb:NVDA+I'
	)
	def script_UIANotificationSwitch(self, gesture):
		self.switch += 1
		if self.switch>1: self.switch = -1
		config.conf['UIANotificationSwitch']['switch'] = self.switch
		ui.message(self.description[self.switch+1])
