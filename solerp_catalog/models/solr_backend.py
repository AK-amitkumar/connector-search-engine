# -*- coding: utf-8 -*-
# © 2016 Akretion (http://www.akretion.com)
# Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp import api, models
from openerp.addons.solerp.unit import exporter
from openerp.addons.connector.session import ConnectorSession


class SolrBackend(models.Model):
    _inherit = 'solr.backend'

    @api.model
    def _scheduler_export_product(self, batch_size=5000):
        templates = self.env['solr.product.template'].search([
            ('sync_state', '=', 'to_update')
            ])
        while templates:
            processing = templates[0:batch_size]
            templates = templates[batch_size:]
            session = ConnectorSession(self._cr, self._uid, self._context)
            exporter.export_record.delay(
                session, 'solr.product.template', processing.ids)
            processing.with_context(connector_no_export=True).write({
                'sync_state': 'scheduled',
                })
