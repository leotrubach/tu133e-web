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


class LocSeries(models.Model):
    name = models.CharField(max_length=20, verbose_name=_('name'))

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _('locomotive series')
        verbose_name_plural = _('locomotive series')


class Locomotive(models.Model):
    number = models.CharField(max_length=20, verbose_name=_('name'))
    series = models.ForeignKey(LocSeries, verbose_name=_('series'))

    def __unicode__(self):
        return '%(series)s %(number)s' % {'series': self.series,
                                          'number': self.number}

    class Meta:
        verbose_name = _('locomotive series')
        verbose_name_plural = _('locomotive series')


class LogEntry(models.Model):
    ord_number = models.IntegerField(verbose_name=_('ord'))
    depo = models.ForeignKey(Depo, verbose_name=_('depo'))
    drive_date = models.DateField(verbose_name=_('drive date'))
    driver = models.ForeignKey(Employee, verbose_name=_('driver'))
    instructor = models.ForeignKey(User, verbose_name=_('instructor'))
    speedometer = models.CharField(max_length=20, 
                                   verbose_name=_('speedometer'))
    loc_series = models.ForeignKey(LocSeries, 
                                   verbose_name=_('locomotive series'))
    loc_number = models.ForeignKey()

    def __unicode__(self):
        pass

    class Meta:
        verbose_name = _('log entry')
        verbose_name_plural = _('log entries')
