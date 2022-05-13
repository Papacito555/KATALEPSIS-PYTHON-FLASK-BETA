(function() {
    'use strict';
    window.addEventListener('load', function() {
      // Fetch all the forms we want to apply custom Bootstrap validation styles to
      var forms = document.getElementsByClassName('needs-validation');
      // Loop over them and prevent submission
      var validation = Array.prototype.filter.call(forms, function(form) {
        form.addEventListener('submit', function(event) {
          if (form.checkValidity() === false) {
            event.preventDefault();
            event.stopPropagation();
          }
          form.classList.add('was-validated');
        }, false);
      });
    }, false);
  })();
  
  /*

  document.addEventListener('DOMContentLoaded', function () {
    // Adjunte el detector de eventos `change` al checkbox
    document.getElementById('billing-checkbox').onchange = toggleBilling;
  }, false);
  
  function toggleBilling() {
    // Seleccione los campos de texto de facturación
    var billingItems = document.querySelectorAll('#billing input[type="text"]');
  
    // Alternar los campos de texto de facturación
    for (var i = 0; i < billingItems.length; i++) {
      billingItems[i].disabled = !billingItems[i].disabled;
    }
  } 
  */
  var discounted = document.getElementById('inlineRadio2');
  var no_discounted = document.getElementById('billing-checkbox')
  var discount_percentage = document.getElementById('certifica')
  
  function updateStatus() {
    if (discounted.checked) {
      discount_percentage.disabled = true;
    } else {
      discount_percentage.disabled = false;
    }
  }
  
  discounted.addEventListener('change', updateStatus)
  no_discounted.addEventListener('change', updateStatus)