$(document).ready(function() {
  $("#submit").on("click", function() {
    $proname = $('input[name="proname"]').val();
    $protype = $('input[name="protype"]').val();
    $proquantity = $('input[name="proquantity"]').val();
    if ($proname == "" || $protype == "" || $proquantity == "") {
      alert("Please complete field");
    } else {
      $.ajax({
        type: "POST",
        url: "insert",
        data: {
          proname: $proname,
          protype: $protype,
          proquantity: $proquantity,
          csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(data) {
          alert("Save Data");
          $('input[name="proname"]').val("");
          $('input[name="protype"]').val("");
          $('input[name="proquantity"]').val("");
          window.location = "/products";
        }
      });
    }
  });
  $("#editsubmit").on("click", function() {
    $proname = $('input[name="proname"]').val();
    $protype = $('input[name="protype"]').val();
    $proquantity = $('input[name="proquantity"]').val();
    $proid = $('input[name="proid"]').val();
    if ($proname == "" || $protype == "" || $proquantity == "") {
      alert("Please complete field");
    } else {
      $.ajax({
        type: "POST",
        url: "http://localhost:8000/products/update",
        data: {
          proid: $proid,
          proname: $proname,
          protype: $protype,
          proquantity: $proquantity,
          csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(data) {
          alert("Data updated");
          window.location = "/products";
        }
      });
    }
  });
});

$(".tic").click(function() {
  $no = $(this).val();
  $.ajax({
    type: "POST",
    url: "http://localhost:8000/products/checktic",
    data: {
      numb: $no,
      csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
    },
    success: function(data) {
      console.log(data);
    }
  });
  //}
});
