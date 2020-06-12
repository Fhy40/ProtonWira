// Get a reference to the progress bar, wrapper & status label
var progress_checker_ajax
var has_run = 0

function getProgress(){
    $.ajax({url : '/testkitchen', type : 'POST', success: function (data) {
        console.log(data['progress']);
        progress_value = data['progress']
        progress_checker_ajax = data['progress']
        progress_status = data['status']
        width_text = "width: " + progress_value + '%'
        document.getElementById("current_status_text").innerHTML = progress_status
        document.getElementById("progressbar").setAttribute("style", width_text);
        document.getElementById("progressbar").setAttribute("aria-valuenow:", progress_value);
        document.getElementById("progressbar").innerHTML = progress_value + '%'
    }})
    if (has_run == 0){
        if (progress_checker_ajax != "100") {
            setTimeout(getProgress,1000);
            console.log("Server is still processing")
          } else {
              has_run = 1
              console.log("Process Complete")
              console.log(progress_checker_ajax)
          }
        console.log(has_run)
    } else {
        setTimeout(getProgress,1000);
        console.log("New Request")
        has_run = 0
    }
}