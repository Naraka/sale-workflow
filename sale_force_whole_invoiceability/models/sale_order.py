# Copyright 2021 Tecnativa - David Vidal
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def force_lines_to_invoice_policy_order(self):
        """Wrapper to launch the private method from UI"""
        if not self.env.user.has_group("sales_team.group_sale_manager"):
            raise UserError(
                self.env._(
                    "Only Sales Managers are allowed to force the lines to invoice"
                )
            )
        if self.state != "sale":
            raise UserError(
                self.env._(
                    "You can't perform this action over a sale order in this state"
                )
            )
        if self.invoice_count:
            raise UserError(
                self.env._(
                    "You can't perform this action once the order has been "
                    "invoiced once already"
                )
            )
        self._force_lines_to_invoice_policy_order()
