var g_user_x
var g_user_y
var g_user_z
function dilation_factors(obj){
    g_user_x = $('#id_dilation_x').val();
    g_user_y = $('#id_dilation_y').val();
    g_user_z = $('#id_dilation_z').val();
    $.ajax({
        url: '/ajax/dilation/',
        data: {
            'x_factor' : g_user_x,
            'y_factor' : g_user_y,
            'z_factor' : g_user_z,
        },
        datatype:'json',
        success:function (data) {
 
            $("#id_tip").html("<span style='color:Green'>Import Successful</span>");
        }
    })
}