odoo.define('extend_lead.ListView', function (require){ "use strict";
    var core = require('web.core');
    var QWeb = core.qweb;

    var ListView = core.view_registry.get('list');

    // Use include to override the render method
    ListView.List.include({
         render: function () {
                var self = this;
                this.$current.html(
                    QWeb.render('ListView.rows', _.extend({}, this, {
                        render_cell: function () {
                            return self.render_cell.apply(self, arguments); }
                })));

                 //Change amount of empty rows to one for extend_lead.obstacle only
                if (this.view.model == "extend_lead.obstacle"){
                    this.pad_table_to(1);
                }
                else{
                    this.pad_table_to(4);
                }
            }
    });
});