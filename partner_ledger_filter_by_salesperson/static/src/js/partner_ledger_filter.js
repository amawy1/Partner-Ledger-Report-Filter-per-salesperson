odoo.define('partner_ledger_filter_by_salesperson.custom_partner_ledger', function (require) {
    'use strict';

    var AccountReport = require('account_reports.account_report');
    var core = require('web.core');
    var _t = core._t;

    AccountReport.include({
        render_searchview_buttons: function () {
            this._super.apply(this, arguments);
            var self = this;

            if (!this.$searchview_buttons.find('.js_account_salesperson_m2m .o_m2m_selection').children('select').length) {
                var $input = $('<select/>', {
                    class: 'o_input',
                    name: 'salesperson_id',
                    multiple: 'multiple',
                    'aria-hidden': 'true'
                });

                this.$searchview_buttons.find('.js_account_salesperson_m2m .o_m2m_selection').append($input);

                $input.append(new Option(_t("All Salespersons"), 'all'));

                this._rpc({
                    model: 'res.users',
                    method: 'search_read',
                    fields: ['id', 'name']
                }).then(function (users) {
                    users.forEach(function (user) {
                        $input.append(new Option(user.name, user.id));
                    });

                    $input.select2({
                        width: '100%',
                        placeholder: _t("Select Salesperson"),
                    });

                    if (self.report_options.salesperson_id) {
                        $input.val(self.report_options.salesperson_id).trigger('change');
                    }

                    self.$searchview_buttons.find('.btn-salesperson-filter').on('click', function () {
                        var selectedValues = $input.val();
                        self.update_salesperson_filter(selectedValues);
                    });
                });
            }
        },

        update_salesperson_filter: function (selectedValues) {
            if (selectedValues.includes('all')) {
                this.report_options.salesperson_id = null;
            } else {
                this.report_options.salesperson_id = selectedValues;
            }
            this.reload();
        }
    });
});
