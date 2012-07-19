from django.db import models
from django.utils.translation import ugettext_lazy as _


class Depo(models.Model):
	name = models.CharField(verbose_name=_('name'))

	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		verbose_name = _('depo')
		verbose_name_plural = _('depos')


class Employee(models.Model):
	full_name = models.CharField(max_length=100, verbose_name=_('full name'))

	def __unicode__(self):
		return unicode(self.full_name)

	class Meta:
		verbose_name = _('employee')
		verbose_name_plural = _('employees')


class LogEntry(models.Model):
	depo = models.ForeignKey(Depo, verbose_name=_('depo'))

	def __unicode__(self):
		pass

	class Meta:
		verbose_name = _('log entry')
		verbose_name_plural = _('log entries')
