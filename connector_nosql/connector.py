# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Raphaël Valyi
#    Copyright 2013 Akretion LTDA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.addons.connector.connector import ConnectorEnvironment


class ConnectorNosqlEnvironment(ConnectorEnvironment):

    def __init__(self, index_record, session, model_name):
        self.index_record = index_record
        super(ConnectorNosqlEnvironment, self).__init__(
            index_record.backend_id, session, model_name)


def get_environment(session, model_name, index_id):
    """ Create an environment to work with. """
    index_record = session.env['nosql.index'].browse(index_id)
    env = ConnectorNosqlEnvironment(index_record, session, model_name)
    return env
