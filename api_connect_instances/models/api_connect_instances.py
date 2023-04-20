import logging
import requests

from odoo import fields, models, _
from odoo.exceptions import UserError
from odoo.tools.misc import ustr

_logger = logging.getLogger(__name__)


class APIConnectInstances(models.Model):
    _name = 'api.connect.instances'
    _inherit = ['mail.thread']
    _description = 'The config server information for API Viettel Post'

    name = fields.Char(string='Name', required=True, tracking=True)
    code = fields.Char(string='Code', required=True, tracking=True)
    host = fields.Char(string='Host', required=True, tracking=True)
    token = fields.Text(string='Token', tracking=True, readonly=True)
    active = fields.Boolean(string='Active', default=True, tracking=True)
    user_name = fields.Char(string='Username', tracking=True)
    password = fields.Char(string='Password')
    endpoint_ids = fields.One2many('api.endpoint.config', 'instance_id', string='Endpoints')

    def btn_test_connection(self):
        self.ensure_one()
        try:
            request = requests.get(self.host, timeout=3)
            _logger.info(f'{request}')
        except Exception as e:
            raise UserError(_(f'Connection Test Failed! Here is what we got instead:\n {ustr(e)}'))
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": _("Connection test successfully!"),
                "type": "success",
                "message": _("Everything seems properly set up!"),
                "sticky": False,
            },
        }

    def generate_client_api(self, carrier_code: str):
        raise NotImplementedError(_('Please implement the function to generate client API before use.'))


class APIConnectHistory(models.Model):
    _name = 'api.connect.history'
    _description = 'Logging request api to ViettelPost'
    _order = 'create_date desc'

    name = fields.Char(string='Request', required=True, readonly=True)
    status = fields.Integer(string='Status', required=True, readonly=True)
    message = fields.Char(string='Message', required=True, readonly=True)
    url = fields.Char(string='Url', required=True, readonly=True)
    method = fields.Char(string='Method', required=True, readonly=True)
    body = fields.Text(string='Body', readonly=True)
    request_id = fields.Char(string='Request Id', required=True, readonly=True)


class APIEndpointConfig(models.Model):
    _name = 'api.endpoint.config'
    _inherit = ['mail.thread']
    _description = 'Configuration dynamic endpoint for host when there is a change of routes from ViettelPost. '

    endpoint = fields.Char(string='Endpoint', required=True, tracking=True)
    name = fields.Char(string='Function name', required=True, readonly=True, tracking=True)
    instance_id = fields.Many2one('api.connect.instances', string='Instance', tracking=True)
    host = fields.Char(related='instance_id.host', string='Host')
    description = fields.Text(string='Description')
