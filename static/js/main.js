// Get a reference to the progress bar, wrapper & status label
var progress_checker_ajax

function getProgress(){
    $.ajax({url : '/testkitchen', type : 'POST', success: function (data) {
        console.log(data['progress']);
        progress_value = data['progress']
        progress_checker_ajax = data['progress']
        width_text = "width: " + progress_value + '%'
        document.getElementById("progressbar").setAttribute("style", width_text);
        document.getElementById("progressbar").setAttribute("aria-valuenow:", progress_value);
        document.getElementById("progressbar").innerHTML = progress_value + '%'
    }})
    if (progress_checker_ajax != "100") {
        setTimeout(getProgress,1000);
      }    
        
}