// Script for Short URL form
$(document).on("submit", "#shortener_form", function (event) {
  event.preventDefault();
  $.ajax({
    type: "POST",
    url: "/short_url",
    data: {
      url: $("#url").val(),
      csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
    },
    success: function (data) {
      $("#shorted_url").html("127.0.0.1:8000/" + data);
    },
  });
  $("#copy_button").addClass("active");
  $("#copy_button").removeClass("none");
});

// Script to Copy link from clipboard
function copy(elementId) {
  var inputElement = document.createElement("input");
  inputElement.setAttribute(
    "value",
    document.getElementById(elementId).innerHTML
  );
  document.body.appendChild(inputElement);
  inputElement.select();
  document.execCommand("copy");
  document.body.removeChild(inputElement);
  $(".shorted_url_container").addClass("none");
  window.location.reload();
}
