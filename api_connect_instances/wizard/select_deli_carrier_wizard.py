from odoo import fields, models, api, _


class SelectDeliveryCarrierWizard(models.TransientModel):
    _name = 'select.delivery.carrier.wizard'
    _description = 'This module is used open a popup to select delivery carrier'

    @api.model
    def default_get(self, fields_list):
        values = super(SelectDeliveryCarrierWizard, self).default_get(fields_list)
        if not values.get('deli_order_id') and 'active_model' in self._context and\
                self._context['active_model'] == 'stock.picking':
            values['deli_order_id'] = self._context.get('active_id')
        return values

    deli_order_id = fields.Many2one('stock.picking', required=True, readonly=True)
    deli_carrier_id = fields.Many2one('delivery.carrier', required=True)

    def action_assign_delivery(self):
        raise NotImplementedError(_(f'Subclass needs to be implemented this static method: action_assign_delivery.'))