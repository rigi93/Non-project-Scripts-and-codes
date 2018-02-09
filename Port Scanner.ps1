$netadd = "192.168.1"
$port = 53,67,123,135,137,138,161,445,631,1434
$netaddrange = 1..15

foreach( $n in $netaddrange )
{
	$ip = "{0}.{1}" -F $netadd, $n
	"$ip"
		foreach( $p in $port )
		{
			$soc = new-object System.Net.Sockets.UdpClient
			$soc.client.ReceiveTimeout = 1000
			$soc.Connect($ip,$p)
			$b = new-object System.text.asciiencoding
			$byte = $b.GetBytes("This works")
			$soc.Send($byte,$byte.length)
			$ep = new-object System.Net.ipendpoint([system.net.ipaddress]::Any,0)			
			Try{
				$recbyte = $soc.Receive([ref]$ep)
				[String]$content = $b.GetString($recbyte)
			   }
			Catch {
				[String]$content = $Error[0].ToString()
			}
			if ($content -match "\b existing \b")
			{
			  " Port $p is closed"
			}
			else
			{
			 " Port $p is filtered | open "
			}
			
		}
}