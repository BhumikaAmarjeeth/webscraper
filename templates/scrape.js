$(function(){
   $(".error").hide();
   $("#spinner").hide();
   $("#crawl").click(function(){
        $("#spinner").hide();
        $(".error").hide();
        var start_url = $("#start_url").val();
        
        if (start_url == ''){
            $('#start_url_error').show();
            $('#start_url_error').focus();
            return false;
        }
       
        $("#spinner").show();
        $("#spinner").focus();
        $.ajax({
            type: "GET",
            url: "http://localhost:8080/get_site_scrape?start_url="+start_url,
            success:function(data){
                $("#spinner").hide();
                var blob = new Blob([data])
                var filename ="scrapedData.csv"
//                window.navigator.msSaveBlob(blob, filename);
//                var URL = window.URL || window.webkitURL;
//                var downloadUrl = URL.createObjectURL(blob);

                var a = document.createElement("a");
//                a.href = downloadUrl;
                a.href = window.URL.createObjectURL(blob)
                a.download = filename;
                document.body.appendChild(a);
                a.click();
            }
        });
   });
   return false;
})

//function downloadFile(urlToSend) {
//     var req = new XMLHttpRequest();
//     req.open("GET", urlToSend, true);
//     req.responseType = "blob";
//     req.onload = function (event) {
//         var blob = req.response;
////         var fileName = req.getResponseHeader("fileName") //if you have the fileName header available
//         var link=document.createElement('a');
//         link.href=window.URL.createObjectURL(blob);
//         link.download=fileName;
//         link.click();
//     };
//
//     req.send();
// }
