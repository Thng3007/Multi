var urlParams = new URLSearchParams(window.location.search);
function getLang()
{return urlParams.get('lang');
}
function showInfo()
{
	//var lang="vi-VN";
	var lang=getLang();
	var member=members[urlParams.get('code')][lang];
	$('.myinfo').each(function(i, obj) {		
		$("#"+obj.id).html(member[obj.id]);
	});	
}
$( document ).ready(function() {
    showInfo();
});