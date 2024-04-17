var keys = ['id', 'customer_id', 'first_name', 'last_name', 'company', 'city', 'country', 'phone1', 'phone2', 'email', 'subscription_date', 'website', 'sales_2021', 'sales_2022', 'active'];
var customers = [];
var filteredCustomers = [];

function renderTable() {
    $('#customerTable tbody').empty();
    $.each(filteredCustomers, function(key, item) {
        var row = $('<tr></tr>');
        $.each(keys, function(index, key) {
            var cell = item[key];
            row.append($('<td></td>').text(cell));
        });
        $('#customerTable tbody').append(row);
    });
}

$(document).ready(function() {
    var thead = $('#customerTable thead');
    var tr = $('<tr></tr>');
    $.each(keys, function(index, key) {
        tr.append($('<th></th>').text(key));
    });
    thead.append(tr);

    $.getJSON('/get_customers', function(data) {
        customers = data;
        filteredCustomers = customers;
        console.log(customers[0]);
        renderTable();
    });

    $('#sortByName').click(function() {
        filteredCustomers.sort(function(a, b) {
            return a.last_name.localeCompare(b.last_name);
        });
        renderTable();
    });

    $('#sortById').click(function() {
        filteredCustomers.sort(function(a, b) {
            return a.id - b.id;
        });
        renderTable();
    });

    $('#sortBySubDate').click(function() {
        filteredCustomers.sort(function(a, b) {
            return new Date(a.subscription_date) - new Date(b.subscription_date);
        });
        renderTable();
    });

    $('#filterOption').change(function() {
        var filter = $(this).val();
        if (filter === '2020') {
            filteredCustomers = customers.filter(function(customer) {
                return new Date(customer.subscription_date).getFullYear() === 2020;
            });
        } else if (filter === '2021') {
            filteredCustomers = customers.filter(function(customer) {
                return new Date(customer.subscription_date).getFullYear() === 2021;
            });
        } else if (filter === '2022') {
            filteredCustomers = customers.filter(function(customer) {
                return new Date(customer.subscription_date).getFullYear() === 2022;
            });
        } else {
            filteredCustomers = customers;
        }
        renderTable();
    });
});