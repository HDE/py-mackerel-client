# -*- coding: utf-8 -*-
"""
    mackerel.host
    ~~~~~~~~~~~~~

    Mackerel client implemented by Python.

    Ported from `mackerel-client-ruby`.
    <https://github.com/mackerelio/mackerel-client-ruby>

    :copyright: (c) 2014 Hatena, All rights reserved.
    :copyright: (c) 2016 Iskandar Setiadi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""


class MonitorHost(object):

    def __init__(self, **kwargs):
        """Construct a Monitor with type == 'host'.

        :param name: Monitor name (string)
        :param duration: Monitor interval value, in minutes, between 1 to 5 min (number)
        :param metric: Name of the host metric (string)
        :param operator: Determine the condition of ">" or "<" (string)
        :param warning: Threshold that generate a warning alert (number)
        :param critical: Threshold that generate a critical alert (number)
        :param notification_interval: [Optional] Interval for re-sending notifications (number)
        :param scopes: [Optional] Monitoring target's name (array of string)
        :param exclude_scopes: [Optional] Monitoring exclusion target's name (array of string)
        :param is_mute: [Optional] Whether monitoring is muted or not (boolean)
        """
        self.args = kwargs
        self.type = 'host'
        self.name = kwargs.get('name', None)
        self.duration = kwargs.get('duration', None)
        self.metric = kwargs.get('metric', None)
        self.operator = kwargs.get('operator', None)
        self.warning = kwargs.get('warning', None)
        self.critical = kwargs.get('critical', None)
        self.notification_interval = kwargs.get('notificationInterval', None)
        self.scopes = kwargs.get('scopes', None)
        self.exclude_scopes = kwargs.get('excludeScopes', None)
        self.is_mute = kwargs.get('isMute', None)

    def __repr__(self):
        repr = '<Monitor('
        repr += 'type={0}, name={1}, duration={2}, metric={3}, operator={4}, '
        repr += 'warning={5}, critical={6}, notification_interval={7}, scopes={8}, '
        repr += 'exclude_scopes={9}, is_mute={10})'
        return repr.format(self.type,
                           self.name,
                           self.duration,
                           self.metric,
                           self.operator,
                           self.warning,
                           self.critical,
                           self.notification_interval,
                           self.scopes,
                           self.exclude_scopes,
                           self.is_mute)


class MonitorService(object):

    def __init__(self, **kwargs):
        """Construct a Monitor with type == 'service'.

        :param name: Monitor name (string)
        :param service: Name of the service targeted by monitoring (string)
        :param duration: Monitor interval value, in minutes, between 1 to 5 min (number)
        :param metric: Name of the host metric (string)
        :param operator: Determine the condition of ">" or "<" (string)
        :param warning: Threshold that generate a warning alert (number)
        :param critical: Threshold that generate a critical alert (number)
        :param notification_interval: [Optional] Interval for re-sending notifications (number)
        :param is_mute: [Optional] Whether monitoring is muted or not (boolean)
        """
        self.args = kwargs
        self.type = 'service'
        self.name = kwargs.get('name', None)
        self.service = kwargs.get('service', None)
        self.duration = kwargs.get('duration', None)
        self.metric = kwargs.get('metric', None)
        self.operator = kwargs.get('operator', None)
        self.warning = kwargs.get('warning', None)
        self.critical = kwargs.get('critical', None)
        self.notification_interval = kwargs.get('notificationInterval', None)
        self.is_mute = kwargs.get('isMute', None)

    def __repr__(self):
        repr = '<Monitor('
        repr += 'type={0}, name={1}, service={2}, duration={3}, metric={4}, '
        repr += 'operator={5}, warning={6}, critical={7}, '
        repr += 'notification_interval={8}, is_mute={9})'
        return repr.format(self.type,
                           self.name,
                           self.service,
                           self.duration,
                           self.metric,
                           self.operator,
                           self.warning,
                           self.critical,
                           self.notification_interval,
                           self.is_mute)


class MonitorExternal(object):

    def __init__(self, **kwargs):
        """Construct a Monitor with type == 'external'.

        :param name: Monitor name (string)
        :param url: Monitoring target URL (string)
        :param service: [Optional] Name of the service targeted by monitoring (string)
        :param notification_interval: [Optional] Interval for re-sending notifications (number)
        :param response_time_warning: [Optional] Time threshold for Warning in ms (number)
        :param response_time_critical: [Optional] Time threshold for Critical in ms (number)
        :param response_time_duration: [Optional] Monitor the avg of requests, 1-5 min (number)
        :param contains_string: [Optional] String which should be contained by the response body (string)
        :param max_check_attempts: [Optional] number of consecutive Warning/Critical before alert is made (number)
        :param certification_expiration_warning: [Optional] Number of days before expiration (number)
        :param certificate_expiration_critical: [Optional] Number of days before expiration (number)
        :param is_mute: [Optional] Whether monitoring is muted or not (boolean)
        """
        self.args = kwargs
        self.type = 'external'
        self.name = kwargs.get('name', None)
        self.url = kwargs.get('url', None)
        self.service = kwargs.get('service', None)
        self.notification_interval = kwargs.get('notificationInterval', None)
        self.response_time_warning = kwargs.get('responseTimeWarning', None)
        self.response_time_critical = kwargs.get('responseTimeCritical', None)
        self.response_time_duration = kwargs.get('responseTimeDuration', None)
        self.contains_string = kwargs.get('containsString', None)
        self.max_check_attempts = kwargs.get('maxCheckAttempts', None)
        self.certificate_expiration_warning = \
            kwargs.get('certificateExpirationWarning', None)
        self.certificate_expiration_critical = \
            kwargs.get('certificateExpirationCritical', None)
        self.is_mute = kwargs.get('isMute', None)

    def __repr__(self):
        repr = '<Monitor('
        repr += 'type={0}, name={1}, url={2}, service={3}, notification_interval={4}, '
        repr += 'response_time_warning={5}, response_time_critical={6}, '
        repr += 'response_time_duration={7}, contains_string={8}, '
        repr += 'max_check_attempts={9}, certificate_expiration_warning={10}, '
        repr += 'certificate_expiration_critical={11}, is_mute={12})'
        return repr.format(self.type,
                           self.name,
                           self.url,
                           self.service,
                           self.notification_interval,
                           self.response_time_warning,
                           self.response_time_critical,
                           self.response_time_duration,
                           self.contains_string,
                           self.max_check_attempts,
                           self.certificate_expiration_warning,
                           self.certificate_expiration_critical,
                           self.is_mute)


class MonitorConnectivity(object):

    def __init__(self, **kwargs):
        """Construct a Monitor with type == 'connectivity'.

        :param id: Connectivity Id (string)
        :param scopes: [Optional] Monitoring target's name (array of string)
        :param exclude_scopes: [Optional] Monitoring exclusion target's name (array of string)
        :param is_mute: [Optional] Whether monitoring is muted or not (boolean)
        """
        self.args = kwargs
        self.type = 'connectivity'
        self.id = kwargs.get('id', None)
        self.scopes = kwargs.get('scopes', None)
        self.exclude_scopes = kwargs.get('excludeScopes', None)
        self.is_mute = kwargs.get('isMute', None)

    def __repr__(self):
        repr = '<Monitor('
        repr += 'type={0}, id={1}, scopes={2}, exclude_scopes={3}, '
        repr += 'is_mute={4})'
        return repr.format(self.type,
                           self.id,
                           self.scopes,
                           self.exclude_scopes,
                           self.is_mute)
