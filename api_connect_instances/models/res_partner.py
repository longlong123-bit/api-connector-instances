import hashlib
import os
from odoo import fields, models


def nonce(length=80, prefix="odoo"):
    rbytes = os.urandom(length)
    return "{}_{}".format(prefix, str(hashlib.sha1(rbytes).hexdigest()))


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Configuration partner Webhook'

    token = fields.Char(string='Token', help='Authorization of delivery carrier', tracking=True)
    type = fields.Selection(selection_add=[('webhook_service', 'Webhook Service')])

    def get_access_token(self):
        self.write({'token': nonce()})
